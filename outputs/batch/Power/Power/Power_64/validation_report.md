# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_64`
- **Input XML**: `outputs/batch/Power/Power/Power_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 43 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [24-372] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-348] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-331] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-347] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [258-286] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-351] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-396] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-352] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-311] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-332] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-349] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-347] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-350] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-319] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-327] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-350] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-186] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-300] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-308] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-303] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-416] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.