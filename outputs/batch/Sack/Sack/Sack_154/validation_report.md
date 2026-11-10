# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_154`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_154/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [93-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [140-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [112-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-150] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-140] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-134] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.