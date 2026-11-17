# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_50`
- **Input XML**: `outputs/batch/Power/Power/Power_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [26-238] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-227] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-259] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [119-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-236] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-243] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-218] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-177] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-258] for track '25' has 1 frames without a visible bounding box.
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