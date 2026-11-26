# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_173`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_173/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 18 |
| Player Tracks | 18 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 25 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [105-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-79] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.