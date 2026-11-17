# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_308`
- **Input XML**: `outputs/batch/Power/Power/Power_308/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [12-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-323] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-320] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-302] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-213] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-354] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-360] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-285] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-345] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-371] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-312] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-362] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [156-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-332] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [337-378] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [156-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-272] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-281] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-389] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-378] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-266] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-316] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-320] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-344] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-338] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-280] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-389] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-334] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-345] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-364] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-368] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-335] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-389] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-366] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-361] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-370] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-389] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-356] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-373] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-374] for track '32' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.