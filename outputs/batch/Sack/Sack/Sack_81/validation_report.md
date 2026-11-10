# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_81`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 42 |
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
> - Action 'Action_PreSnap' range [0-124] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [136-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-150] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-138] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '24' has 2 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.