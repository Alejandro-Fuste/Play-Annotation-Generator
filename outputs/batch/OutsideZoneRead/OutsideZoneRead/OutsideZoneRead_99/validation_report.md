# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_99`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [2–16], lower_priority='Action_ZoneBlock' annotated_start=5, effective_Action_ZoneBlock_start=17.
> - Action 'Action_None' range [2-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-120] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-29] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [87-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-133] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-124] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [108-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-51] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-63] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-129] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-136] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [117-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-143] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.