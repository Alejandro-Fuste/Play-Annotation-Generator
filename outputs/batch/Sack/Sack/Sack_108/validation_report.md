# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_108`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
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
> - Action 'Action_PreSnap' range [0-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [137-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [142-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [147-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-63] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [118-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-149] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '18' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.