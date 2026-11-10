# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_129`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 20 |
| Ball Tracks | 1 |
| CSV events parsed | 11 |
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
> - Action 'Action_PreSnap' range [0-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [91-120] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-94] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '20' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.