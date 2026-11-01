# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_333`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_333/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [28–40], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=41.
> - Action 'Action_None' range [28-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-39] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-46] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-133] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-67] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-102] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-139] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-80] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [28-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-55] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-71] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-38] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-74] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-143] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [64-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-159] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.