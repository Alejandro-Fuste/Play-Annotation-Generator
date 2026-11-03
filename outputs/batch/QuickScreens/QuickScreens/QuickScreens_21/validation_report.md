# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_21`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_RunAfterCatch' range [79-211] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [36-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-230] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-116] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-206] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [11-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-149] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-145] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
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