# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_112`
- **Input XML**: `outputs/batch/Power/Power/Power_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [13-303] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-234] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-239] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-70] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-211] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [190-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [201-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [212-218] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-308] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-234] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-263] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-329] for track '21' has 3 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.