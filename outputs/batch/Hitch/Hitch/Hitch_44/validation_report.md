# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_44`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [23–36], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [23-71] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [241-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-30] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-140] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-166] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [23-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-129] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-174] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-187] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-77] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-129] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-92] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-156] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-173] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.