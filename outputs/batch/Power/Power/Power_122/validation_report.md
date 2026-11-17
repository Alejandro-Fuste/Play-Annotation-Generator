# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_122`
- **Input XML**: `outputs/batch/Power/Power/Power_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 38 |
| Ball Tracks | 1 |
| CSV events parsed | 11 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 246: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 246: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [15-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-131] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-78] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-53] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [56-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-260] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-269] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-133] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-100] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-269] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-138] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-221] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-222] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-237] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-163] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-256] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-158] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-245] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-254] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-256] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-268] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '38' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.