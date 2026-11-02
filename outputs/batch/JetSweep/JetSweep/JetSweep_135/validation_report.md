# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_135`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_135/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [10–22], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=23.
> - Action 'Action_None' range [10-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-32] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-167] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-164] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [41-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-194] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-63] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
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