# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_302`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_302/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [23–37], lower_priority='Action_ZoneBlock' annotated_start=26, effective_Action_ZoneBlock_start=38.
> - Action 'Action_None' range [23-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [66-183] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-105] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-144] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-69] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-153] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-143] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-117] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-156] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-82] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-118] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-177] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-195] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-202] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-203] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.