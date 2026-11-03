# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_61`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
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
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [75-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [209-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-126] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-207] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-204] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [206-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-25] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-210] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-197] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '27' has 1 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.