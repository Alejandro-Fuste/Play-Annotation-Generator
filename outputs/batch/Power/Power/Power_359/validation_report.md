# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_359`
- **Input XML**: `outputs/batch/Power/Power/Power_359/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-177] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-154] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-162] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [63-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-180] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-86] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-148] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-137] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-167] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-175] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.