# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_37`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-249] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [201-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-209] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [44-119] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [127-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-105] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-116] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-125] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-159] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.