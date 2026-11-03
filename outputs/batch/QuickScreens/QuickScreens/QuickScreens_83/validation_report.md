# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_83`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [113-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [68-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [162-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-54] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-53] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-173] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-170] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.