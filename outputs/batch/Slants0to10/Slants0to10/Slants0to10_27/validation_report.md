# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Slants0to10_27`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 15, Column 'Pass Block': Could not parse frame number from '-' in entry '-,OL'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [91-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [237-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-89] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-93] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-72] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-85] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [50-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-55] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-189] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-182] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.