'''
Metrics table class for VEP 
'''
from metrics.mixins import CustomToolMd5TypeMixin
from metrics.base_metrics import CWLMetricsMd5Tool

from utils.hash_md5 import get_gz_md5 
from cdis_pipe_utils import postgres

class VEPMetricsTable(CustomToolMd5TypeMixin, postgres.Base):

    __tablename__ = 'vep_metrics'

class VEPMetricsTool(CWLMetricsMd5Tool):
    def __init__(self, time_file, normal_id, tumor_id, input_uuid, output_uuid, case_id, engine, input_file):
        super(VEPMetricsTool,self).__init__(time_file, normal_id, tumor_id, input_uuid, output_uuid, case_id, engine, input_file)
        self.tool  = 'vep'
        self.files = [normal_id, tumor_id]

    def add_metrics(self):
        time_metrics = self.get_time_metrics()
        md5          = self.get_gz_md5()
        metrics      = VEPMetricsTable(case_id           = self.case_id,
                                       vcf_id            = self.output_uuid,
                                       src_vcf_id        = self.input_uuid,
                                       tool              = self.tool,
                                       files             = self.files,
                                       systime           = time_metrics['system_time'],
                                       usertime          = time_metrics['user_time'],
                                       elapsed           = time_metrics['wall_clock'],
                                       cpu               = time_metrics['percent_of_cpu'],
                                       max_resident_time = time_metrics['maximum_resident_set_size'],
                                       md5               = md5)
        postgres.create_table(self.engine, metrics)
        postgres.add_metrics(self.engine, metrics)
