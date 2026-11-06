# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_142`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
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
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [28–40], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=41.
> - Action 'Action_None' range [28-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-102] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-192] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '4' starts at frame 119, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [119-169] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-118] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-191] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-56] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-57] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-191] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-134] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-174] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-176] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.