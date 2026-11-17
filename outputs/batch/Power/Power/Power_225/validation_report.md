# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_225`
- **Input XML**: `outputs/batch/Power/Power/Power_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [11-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-398] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-430] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-311] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-294] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-304] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-353] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-314] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-323] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-341] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-407] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-379] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-278] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [280-284] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [289-303] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-289] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [291-293] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-390] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-413] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-428] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-347] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-373] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-386] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-347] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-296] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-305] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-351] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-369] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [270-314] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-340] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-360] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-325] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-332] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-337] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-341] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-402] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-413] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-420] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-436] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-375] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-449] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-366] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-411] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [417-421] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-430] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-385] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-393] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-400] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-396] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-408] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-420] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-435] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [443-449] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-449] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-406] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.