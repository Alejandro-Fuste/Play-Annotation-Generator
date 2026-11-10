# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_134`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 270: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-143] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-136] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [81-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [107-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [127-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [104-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-105] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-122] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-168] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '27' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.