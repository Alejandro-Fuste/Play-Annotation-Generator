# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_211`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_211/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 21 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '0' has invalid range: start=213, end=197. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '2' has invalid range: start=213, end=192. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=213, end=183. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '10' has invalid range: start=213, end=202. Clamping end to start.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=250, end=239. Clamping end to start.
> - Segment 'Action_Handoff' for track '17' has invalid range: start=241, end=239. Clamping end to start.
> - Action 'Action_PreSnap' range [0-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-197] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-166] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-202] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-100] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-194] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-209] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-178] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '21' has 1 frames without a visible bounding box.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_Handoff' has invalid start frame 241. Video range is [0, 239].
> - Action event 'Action_BallCarry' has invalid start frame 250. Video range is [0, 239].
> - Action event 'Action_None' has invalid start frame 277. Video range is [0, 239].
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_211'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.