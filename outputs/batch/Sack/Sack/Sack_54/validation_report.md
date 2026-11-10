# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_54`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 41 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-84] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-146] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-123] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [126-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [138-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [106-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [118-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.