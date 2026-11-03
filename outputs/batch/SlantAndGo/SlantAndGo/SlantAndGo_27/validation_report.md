# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_27`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [4–16], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=17.
> - Action 'Action_None' range [4-49] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [51-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SellRoute' range [46-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [73-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [76-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [70-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-124] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-148] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-16] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [4-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 4, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [4-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-99] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-100] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-134] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-104] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-175] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '43' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.