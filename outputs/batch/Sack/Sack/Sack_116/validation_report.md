# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_116`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
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
> - Action 'Action_PreSnap' range [0-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [96-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-64] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-120] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-95] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '19' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.