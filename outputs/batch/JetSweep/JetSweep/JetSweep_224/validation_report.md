# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_224`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_224/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 450: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [66-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-145] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [68-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-216] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [66-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-111] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-117] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-215] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '39' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.