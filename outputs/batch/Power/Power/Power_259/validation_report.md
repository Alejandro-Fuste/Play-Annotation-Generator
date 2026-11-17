# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_259`
- **Input XML**: `outputs/batch/Power/Power/Power_259/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 517: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
> - Row 518: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [10-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-351] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-369] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-283] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-311] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-357] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-369] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-287] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-276] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-16] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-306] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-319] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-387] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 255, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [255-359] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-351] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [218-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 255, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [255-375] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-98] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-139] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-308] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-318] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-335] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-356] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-370] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-350] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-356] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-368] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-380] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-373] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-378] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.