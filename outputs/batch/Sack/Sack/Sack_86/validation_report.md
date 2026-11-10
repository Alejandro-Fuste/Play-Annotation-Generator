# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_86`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 31 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [133-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-150] for track '18' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.