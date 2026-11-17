# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_6`
- **Input XML**: `outputs/batch/Power/Power/Power_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [6-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-255] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-304] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-254] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-238] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-285] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-307] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [165-220] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-307] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-251] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-262] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [165-175] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-247] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [165-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [187-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [202-215] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-253] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-240] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-282] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-254] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-302] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-284] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-294] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-276] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-304] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-325] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-324] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.