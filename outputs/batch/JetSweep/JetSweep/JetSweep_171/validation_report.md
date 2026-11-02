# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_171`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '9' (TE1) duration 128 frames exceeds threshold 90 frames [start=100, end=227].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 128 frames exceeds threshold 90 frames [start=100, end=227].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 128 frames exceeds threshold 90 frames [start=100, end=227].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 128 frames exceeds threshold 90 frames [start=100, end=227].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 128 frames exceeds threshold 90 frames [start=100, end=227].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [99–112], lower_priority='Action_ZoneBlock' annotated_start=100, effective_Action_ZoneBlock_start=113.
> - Action 'Action_None' range [99-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-296] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-287] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-230] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-268] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-149] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-296] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-197] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-284] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-270] for track '30' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.