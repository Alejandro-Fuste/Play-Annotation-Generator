# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_82`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-174] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [88-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [106-115] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-209] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-209] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-197] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.