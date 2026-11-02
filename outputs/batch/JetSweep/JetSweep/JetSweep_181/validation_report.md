# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_181`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 124 frames exceeds threshold 90 frames [start=65, end=188].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 124 frames exceeds threshold 90 frames [start=65, end=188].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 124 frames exceeds threshold 90 frames [start=65, end=188].
> - Action 'Action_None' range [57-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-166] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [65-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-130] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-208] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-82] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-195] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-145] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-219] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.