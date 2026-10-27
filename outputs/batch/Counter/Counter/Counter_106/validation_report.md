# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_106`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 95 frames exceeds threshold 90 frames [start=190, end=284].
> - Validation warning: Action 'Action_DownBlock' for track '2' (LT) duration 95 frames exceeds threshold 90 frames [start=190, end=284].
> - Action 'Action_None' range [188-302] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [190-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-305] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-264] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [267-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-302] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-467] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-245] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-266] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-319] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-287] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '9' starts at frame 188, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [188-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-356] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-274] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-301] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-479] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-151] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-70] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-391] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-294] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-262] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-277] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-362] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-376] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-462] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-337] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-314] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-331] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-405] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-368] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-381] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-340] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-479] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-403] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-414] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-428] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-433] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-437] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-447] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-457] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-466] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-415] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-439] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-423] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-446] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [468-469] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-473] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.