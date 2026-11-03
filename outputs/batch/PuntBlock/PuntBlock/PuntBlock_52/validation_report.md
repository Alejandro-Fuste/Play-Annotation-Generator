# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_52`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [8-209] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [70-210] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-210] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-139] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-171] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-107] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [80-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [84-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-112] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-146] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [173-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-119] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-33] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-168] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-196] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-47] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-90] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-176] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-130] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-92] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.