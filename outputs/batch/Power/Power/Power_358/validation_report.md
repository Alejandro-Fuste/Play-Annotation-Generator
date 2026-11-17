# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_358`
- **Input XML**: `outputs/batch/Power/Power/Power_358/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-94] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-121] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-83] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-113] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-119] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-180] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-109] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-125] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-129] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-176] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-50] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '8' starts at frame 27, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [27-27] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [29-37] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [39-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [51-99] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-14] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [28-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [58-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [71-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [27-28] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-34] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [41-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-18] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-146] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-26] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-38] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-72] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-75] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-80] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-142] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-178] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-130] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-179] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '28' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.