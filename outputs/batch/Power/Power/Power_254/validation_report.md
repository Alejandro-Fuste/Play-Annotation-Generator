# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_254`
- **Input XML**: `outputs/batch/Power/Power/Power_254/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-60] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-91] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [46-66] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-133] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-58] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-129] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-112] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-131] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-144] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-132] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.