# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_151`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Segment 'Action_ComboBlock' for track '18' has invalid range: start=230, end=225. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '19' has invalid range: start=230, end=223. Clamping end to start.
> - Action 'Action_PreSnap' range [0-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-302] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-236] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-253] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-263] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-285] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-328] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-327] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-321] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-250] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-286] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-311] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-323] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [230-233] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [236-241] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 286, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [286-288] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-308] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-328] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '25' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.