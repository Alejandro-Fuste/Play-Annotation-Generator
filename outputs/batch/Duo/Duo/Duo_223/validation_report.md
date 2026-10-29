# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Duo_223`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_223/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_ComboBlock' at frame 192 targets track ID '29', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Segment 'Action_ComboBlock' for track '22' has invalid range: start=192, end=182. Clamping end to start.
> - Action 'Action_PreSnap' range [0-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-241] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-42] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [192-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [207-218] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-138] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-221] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-142] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '22' has 1 frames without a visible bounding box.
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
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.