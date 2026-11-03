# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_11`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [19-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-46] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-52] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-241] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-223] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [34-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-264] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [83-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [217-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [225-248] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-175] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-189] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-152] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-138] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-183] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-218] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.