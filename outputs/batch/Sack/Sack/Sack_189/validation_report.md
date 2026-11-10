# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_189`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_189/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-18] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [90-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [128-131] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-78] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-122] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-127] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '20' has 1 frames without a visible bounding box.
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
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.