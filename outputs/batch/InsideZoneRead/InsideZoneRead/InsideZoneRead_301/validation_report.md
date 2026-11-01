# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_301`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_301/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [20–35], lower_priority='Action_ZoneBlock' annotated_start=23, effective_Action_ZoneBlock_start=36.
> - Action 'Action_None' range [20-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-141] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-187] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-119] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-61] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-133] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-131] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-83] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-146] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [44-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [61-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-69] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-30] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [20-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.