# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_83`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 35 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 85, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '150,?'.

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
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [138-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.