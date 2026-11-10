# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_78`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 15 |
| Player Tracks | 15 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 35 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [182-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [205-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-64] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-205] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-200] for track '14' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.