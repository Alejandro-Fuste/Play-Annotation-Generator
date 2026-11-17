# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_20`
- **Input XML**: `outputs/batch/Power/Power/Power_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [3-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-156] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-264] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-189] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-243] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-268] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-102] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-236] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-207] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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