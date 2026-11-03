# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_35`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-70] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [53-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-123] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [141-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-173] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-174] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-163] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-154] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-125] for track '24' has 3 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.