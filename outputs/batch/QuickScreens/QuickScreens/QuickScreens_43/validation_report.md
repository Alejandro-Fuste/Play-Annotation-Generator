# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_43`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ScreenBlock' range [45-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [97-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-135] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-57] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-46] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-51] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-99] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-106] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-192] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-109] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-199] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '36' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.