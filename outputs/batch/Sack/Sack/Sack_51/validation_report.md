# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_51`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 37 |
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
> - Action 'Action_PreSnap' range [0-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [135-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [119-126] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [131-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [142-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [109-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '22' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.