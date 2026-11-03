# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_85`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [26-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [46-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-212] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [26-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-115] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-173] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-94] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '25' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.